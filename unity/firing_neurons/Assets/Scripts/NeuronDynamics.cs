using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class NeuronDynamics : MonoBehaviour
{
    public int[] VE = new int[1000];
    public int[] VR = new int[1000];
    private int readingIndex = 0;

    [Header("Sliders")]
    public Slider ISlider;  // Input current I
    public Slider CSlider;
    public Slider KSlider;
    public Slider ASlider;
    public Slider BSlider;

    [Header("Toggle for RK4")]
    public Toggle RK4Toggle;

    [Header("Fixed Constants")]
    public float vr = -60f;   // Resting potential
    public float vt = -40f;   // Threshold potential
    public float c = -50f;    // Reset value after spike
    public float d = 100f;    // Recovery increment
    public float v_peak = 35f; // Spike threshold

    [Header("Integration Settings")]
    public float h = 1f; // Time step size

    [Header("Firing Effect")]
    public GameObject firingEffectPrefab;  // Particle effect prefab
    public Transform effectSpawnPoint;     // Where effect starts (e.g., head of neuron)
    public Transform[] pathPoints;         // Points along neuron body

    [Header("Live Output")]
    public float v; // Membrane potential
    public float w; // Recovery variable
    public float timeElapsed;

    [Header("Stats UI")]
    public TextMeshProUGUI eulerStatsText;
    public TextMeshProUGUI rk4StatsText;

    // Live values from sliders
    private float I => ISlider.value;
    private float C => CSlider.value;
    private float k => KSlider.value;
    private float a => ASlider.value;
    private float b => BSlider.value;

    void Start()
    {
        // Initial conditions
        v = vr;
        w = 0f;
        timeElapsed = 0f;

    }

    private float simulationStep = 0.001f;  // 1 ms
    private float simTimer = 0f;

    void Update()
    {
        simTimer += Time.deltaTime;

        if (simTimer >= simulationStep)
        {
            if(RK4Toggle.isOn)
            {
                SimulateOneStepRK4();  // Run 1ms worth of neuron dynamics

            }

            else
            {
                Euler(); // Run 1ms worth of neuron dynamics
            }
            
            simTimer -= simulationStep;
        }
    }


    void Euler()
    {
        timeElapsed += simulationStep;

        float vOld = v;

        float dvdt = (k * (v - vr) * (v - vt) - w + I) / C;
        float dwdt = a * (b * (v - vr) - w);

        v += h * dvdt;
        w += h * dwdt;

        if (readingIndex < 1000)
        {
            VE[readingIndex] = (int)v;
            readingIndex++;
        }

        if (readingIndex == 1000)
        {
            int maxV = VE[0];
            int minV = VE[0];
            for (int i = 1; i < 1000; i++)
            {
                if (VE[i] > maxV) maxV = VE[i];
                if (VE[i] < minV) minV = VE[i];
            }

            if (eulerStatsText != null)
            { 
                eulerStatsText.text = $"Euler → Max v: {maxV:F2}\nMin v: {minV:F2}"; 
            }
            readingIndex = 0;
        }

        if (vOld < v_peak && v >= v_peak)
        {
            v = c;
            w += d;

            if (firingEffectPrefab != null && effectSpawnPoint != null)
            {
                GameObject fx = Instantiate(firingEffectPrefab, effectSpawnPoint.position, Quaternion.identity);
                MoveAlongPath pathMover = fx.GetComponent<MoveAlongPath>();
                if (pathMover != null && pathPoints.Length > 0)
                    pathMover.pathPoints = pathPoints;
            }
        }
    }

    void SimulateOneStepRK4()
    {
        float v0 = v;
        float w0 = w;

        // k1
        float k1_v = (k * (v0 - vr) * (v0 - vt) - w0 + I) / C;
        float k1_w = a * (b * (v0 - vr) - w0);

        // k2
        float v1 = v0 + 0.5f * h * k1_v;
        float w1 = w0 + 0.5f * h * k1_w;
        float k2_v = (k * (v1 - vr) * (v1 - vt) - w1 + I) / C;
        float k2_w = a * (b * (v1 - vr) - w1);

        // k3
        float v2 = v0 + 0.5f * h * k2_v;
        float w2 = w0 + 0.5f * h * k2_w;
        float k3_v = (k * (v2 - vr) * (v2 - vt) - w2 + I) / C;
        float k3_w = a * (b * (v2 - vr) - w2);

        // k4
        float v3 = v0 + h * k3_v;
        float w3 = w0 + h * k3_w;
        float k4_v = (k * (v3 - vr) * (v3 - vt) - w3 + I) / C;
        float k4_w = a * (b * (v3 - vr) - w3);

        // Update v and w
        v += (h / 6f) * (k1_v + 2f * k2_v + 2f * k3_v + k4_v);
        w += (h / 6f) * (k1_w + 2f * k2_w + 2f * k3_w + k4_w);

        if (readingIndex < 1000)
        {
            VR[readingIndex] = (int)v;
            readingIndex++;
        }

        if (readingIndex == 1000)
        {
            int maxV = VR[0];
            int minV = VR[0];
            for (int i = 1; i < 1000; i++)
            {
                if (VR[i] > maxV) maxV = VR[i];
                if (VR[i] < minV) minV = VR[i];
            }

            if (rk4StatsText != null)
            { 
                rk4StatsText.text = $"RK4 → Max v: {maxV:F2}\nMin v: {minV:F2}"; 
            }
            readingIndex = 0;
        }

        // Spike condition
        if (v >= v_peak)
        {
            v = c;
            w += d;

            if (firingEffectPrefab != null && effectSpawnPoint != null)
            {
                GameObject fx = Instantiate(firingEffectPrefab, effectSpawnPoint.position, Quaternion.identity);
                MoveAlongPath pathMover = fx.GetComponent<MoveAlongPath>();
                if (pathMover != null && pathPoints.Length > 0)
                    pathMover.pathPoints = pathPoints;
            }
        }
    }

}


