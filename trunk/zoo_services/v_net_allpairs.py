#####################################################
# This service was generated using wps-grass-bridge #
#####################################################
import ZOOGrassModuleStarter as zoo
def v_net_allpairs(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.net.allpairs", inputs, outputs)
    return 3
