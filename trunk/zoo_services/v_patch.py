import ZOOGrassModuleStarter as zoo
def v_patch(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.patch", inputs, outputs)
    return 1
