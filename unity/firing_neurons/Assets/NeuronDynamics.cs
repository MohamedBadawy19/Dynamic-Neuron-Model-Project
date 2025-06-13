using UnityEngine;
using UnityEngine.UI;

public class NeuronDynamics : MonoBehaviour
{
    [Header("Sliders (Link These in Inspector)")]
    public Slider ISlider;  // Input current I
    public Slider CSlider;
    public Slider KSlider;
    public Slider ASlider;
    public Slider BSlider;

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

    private float simulationStep = 0.001f;  // 1 ms in seconds
    private float simTimer = 0f;

    void Update()
    {
        simTimer += Time.deltaTime;

        while (simTimer >= simulationStep)
        {
            SimulateOneStep(); // Run 1ms worth of neuron dynamics
            simTimer -= simulationStep;
        }
    }


    void SimulateOneStep()
    {
        timeElapsed += simulationStep;

        float vOld = v;

        float dvdt = (k * (v - vr) * (v - vt) - w + I) / C;
        float dwdt = a * (b * (v - vr) - w);

        v += h * dvdt;
        w += h * dwdt;

        Debug.Log("v = " + v + ", w = " + w);

        if (vOld < v_peak && v >= v_peak)
        {
            //Debug.Log("Neuron Spike!");
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


