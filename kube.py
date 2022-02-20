from kubernetes import client, config

def kube():
  # Configs can be set in Configuration class directly or using helper utility
  config.load_kube_config()

  return client.CoreV1Api()

def kube_running_pods():
  kubepy = kube()

  pods = kubepy.list_pod_for_all_namespaces(watch=False)
  return pods
