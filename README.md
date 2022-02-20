# askjiggy

Slack bot to interact with my Kubernetes cluster

## Command: `/cycle`

### Actions List

Description: List all pods in all Namespaces

Use: `/cycle list`

Output:

  ```text
  List of all running pods!

  NAMESPACE    STATUS    POD
  kube-system    Running    coredns-78fcd69978-8qb6m
  kube-system    Running    coredns-78fcd69978-xwgv7
  kube-system    Running    etcd-docker-desktop
  kube-system    Running    kube-apiserver-docker-desktop
  kube-system    Running    kube-controller-manager-docker-desktop
  kube-system    Running    kube-proxy-f9njm
  kube-system    Running    kube-scheduler-docker-desktop
  kube-system    Running    storage-provisioner
  kube-system    Running    vpnkit-controller
  ```

### Actions: Pod

Description: Cycle the pod matching name.

Use: `/cycle pod coredns-78fcd69978-8qb6m`

Output:

  ```text
  TODO: Still in phase
  ```

## Resources:

* [Kubernetes](https://github.com/kubernetes-client/python/)
* [Slack Bolt Getting Started](https://slack.dev/bolt-python/tutorial/getting-started#setting-up-events)
* [Slack Bolt Message Format](https://api.slack.com/reference/block-kit/blocks#section)
* [Slack Block Kit Builder](https://app.slack.com/block-kit-builder/)
