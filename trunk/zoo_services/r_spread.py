import ZOOGrassModuleStarter as zoo
def r_spread(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.spread", inputs, outputs)
    return 1
