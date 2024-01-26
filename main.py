import copy
import sys

from kubernetes import client, config

_JOB_MANIFEST =  {
    "apiVersion": "batch/v1",
    "kind": "Job",
    "metadata": {
        "name": "fake-bg-task-<ID>",
    },
    "spec": {
        "ttlSecondsAfterFinished": 10,
        "template": {
            "spec": {
                "containers": [{
                    "name": "fake-bg-task",
                    "image": "<docker_username>/fake_bg_task",
                }],
                "restartPolicy": "Never",
            }
        },
        "backoffLimit": 0,
    }
}


def _create_job(api_instance, docker_username, job_id: int):
    manifest = copy.deepcopy(_JOB_MANIFEST)
    manifest["metadata"]["name"] = manifest["metadata"]["name"].replace("<ID>", str(job_id))
    manifest["spec"]["template"]["spec"]["containers"][0]["image"] = manifest["spec"]["template"]["spec"]["containers"][0]["image"].replace("<docker_username>", docker_username)
    api_response = api_instance.create_namespaced_job(
        body=manifest,
        namespace="default"
    )
    print("Job created. status='%s'" % str(api_response.status))



def main():
    docker_username = sys.argv[1]

    config.load_kube_config()
    api_client = client.BatchV1Api()

    for i in range(10):
        _create_job(api_client, docker_username, i)

if __name__ == "__main__":
    main()
