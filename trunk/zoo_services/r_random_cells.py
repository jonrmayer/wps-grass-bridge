import ZOOGrassModuleStarter as zoo
def r_random_cells(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.random.cells", inputs, outputs)
    return 1
