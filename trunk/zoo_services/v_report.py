#####################################################
# This service was generated using wps-grass-bridge #
#####################################################
import ZOOGrassModuleStarter as zoo
def v_report(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.report", inputs, outputs)
    return 3
