import ZOOGrassModuleStarter as zoo
def v_to_points(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.to.points", inputs, outputs)
    return 1
