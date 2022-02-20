from kube import kube_running_pods

def grab_all_running():
  str =  grab_str()
  format_msg = {
    "blocks": [
      {
        "type": "header",
        "text": {
          "type": "plain_text",
          "text": "List of all running pods!"
        }
      },
      {
        "type": "section",
        "text": {
          "type": "mrkdwn",
          "text": "```" + str + "```"
        }
      }
    ]
  }

  return format_msg

def grab_str():
  pods = kube_running_pods()
  str =  "NAMESPACE\tSTATUS\tPOD\n"
  for i in pods.items:
    name = i.metadata.name
    namespace = i.metadata.namespace
    status = i.status.phase

    str = str + "%s\t%s\t%s\n" % (namespace, status, name)

  return str
