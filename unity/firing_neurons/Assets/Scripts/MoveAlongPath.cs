using UnityEngine;

public class MoveAlongPath : MonoBehaviour
{
    public Transform[] pathPoints;
    public float speed = 5f;
    private int currentPoint = 0;

    void Update()
    {
        if (pathPoints.Length == 0) return;

        Transform target = pathPoints[currentPoint];
        transform.position = Vector3.MoveTowards(transform.position, target.position, speed * Time.deltaTime);

        if (Vector3.Distance(transform.position, target.position) < 0.1f)
        {
            currentPoint++;
            if (currentPoint >= pathPoints.Length)
                Destroy(gameObject); // reached end, destroy effect
        }
    }
}
