import ZOOGrassModuleStarter as zoo
def v_net_iso(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.net.iso", inputs, outputs)
    return 1
