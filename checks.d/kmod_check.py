import subprocess

from checks import AgentCheck

class KernelModuleCheck(AgentCheck):
  def check(self, instance):
    prefix = 'kmodload'
    name = instance['name']
    module_size = instance.get('collect_module_size', True)
    try:
      res = subprocess.check_output('lsmod', stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
      self.service_check(prefix + '.' + name, AgentCheck.WARNING, message=str(e))
    except OSError as e:
      self.service_check(prefix + '.' + name, AgentCheck.WARNING, message=str(e))
    else:
      for row in res.split('\n'):
        if len(row) > 0:
          fields = row.split()
          if fields[0] != 'Module' and fields[0] == name:
            self.service_check(prefix + '.' + name, AgentCheck.OK)
            if module_size:
              self.gauge(prefix + '.size', fields[1], tags=[prefix, 'module:' + name])
            return

      self.service_check(prefix + '.' + name, AgentCheck.CRITICAL)
