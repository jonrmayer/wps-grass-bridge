import ZOOGrassModuleStarter as zoo
def v_net_centrality(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.net.centrality", inputs, outputs)
    return 1
