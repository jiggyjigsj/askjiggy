from kube import kube_running_pods

def isrunning(pod):
  pods = kube_running_pods()
  running = False
  for i in pods.items:
    if i.metadata.name == pod:
      running = True

  return running
