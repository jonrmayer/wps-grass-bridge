import ZOOGrassModuleStarter as zoo
def r_sim_sediment(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.sim.sediment", inputs, outputs)
    return 1
