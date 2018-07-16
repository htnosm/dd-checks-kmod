# dd-checks-kmod

Custom check of kernel module load state for Datadog.

## Overview

checked the module is loaded and collect size of loaded modules from lsmod.

## Setup

```
# DATADOG_AGENT_ROOT_DIR
## version 5: /etc/dd-agent
## version 6: /etc/datadog-agent

{DATADOG_AGENT_ROOT_DIR}/
.
├── checks.d
│   ├── kmod_check.py
│   ...
├── conf.d
│   ├── kmod_check.yaml
│   ...
```

## Data Collected

### Metrics

| Name | Units | Description |
| :--- | :---: | :--- |
| kmodload.size | bytes | The size of the module (not memory used). |

metrics are per instance configured in kmod_check.yaml, and are tagged module:<instance_name>.

### Events

The Process check does not include any events at this time.

### Service Checks

kmodload:

The Agent submits this custom check for each instance in kmod_check.yaml.
tagging each with module:<instance_name>

module:<instance_name> whose status is:

- CRITICAL when it not exists on lsmod.
- OK when it exists on lsmod.
- Other exceptions return Warning.
