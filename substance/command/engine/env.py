from substance.monads import *
from substance.logs import *
from substance import (Engine, Command)
from substance.exceptions import (SubstanceError)

class Env(Command):

  def getUsage(self):
    return "substance engine env [ENGINE NAME]"
 
  def getHelpTitle(self):
    return "Print the shell variables to set up the local docker client environment"

  def getShellOptions(self, optparser):
    return optparser

  def main(self):

    name = self.getInputName()

    self.core.loadEngine(name) \
      .bind(Engine.loadConfigFile) \
      .bind(self.outputDockerEnv) \
      .catch(self.exitError)

  def outputDockerEnv(self, engine):
    publicIP = engine.getPublicIP()
    port = engine.getDockerPort()
    print("export DOCKER_API_VERSION=\"1.19\"")   
    print("export DOCKER_HOST=\"%s\"" % (engine.getDockerURL()))
    print("export DOCKER_TLS_VERIFY=\"\"")
    return OK(None)
