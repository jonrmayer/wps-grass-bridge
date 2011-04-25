# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class r_neighbors(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'r.neighbors', title = 'Makes each cell category value a function of the category values assigned to the cells around it, and stores new cell values in an output raster map layer.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'raster'}, {'type': 'simple', 'title': 'algebra'}, {'type': 'simple', 'title': 'statistics'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/r.neighbors.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Name of input raster map', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'image/png'}, {'mimeType': 'image/gif'}, {'mimeType': 'image/jpeg'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])
    self.addComplexInput(identifier = 'selection', title = 'Name of an input raster map to select the cells which should be processed', minOccurs = 0, maxOccurs = 1, formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'image/png'}, {'mimeType': 'image/gif'}, {'mimeType': 'image/jpeg'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])
    self.addLiteralInput(identifier = 'method', title = 'Neighborhood operation', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "average", allowedValues = ['average', 'median', 'mode', 'minimum', 'maximum', 'range', 'stddev', 'sum', 'variance', 'diversity', 'interspersion', 'quart1', 'quart3', 'perc90', 'quantile'])
    self.addLiteralInput(identifier = 'size', title = 'Neighborhood size', minOccurs = 0, maxOccurs = 1, type = type(0), default = 3)
    self.addLiteralInput(identifier = 'title', title = 'Title of the output raster map', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addComplexInput(identifier = 'weight', title = 'Text file containing weights', minOccurs = 0, maxOccurs = 1, formats = [{'mimeType': 'text/plain'}])
    self.addLiteralInput(identifier = 'gauss', title = 'Sigma (in cells) for Gaussian filter', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'quantile', title = 'Quantile to calculate for method=quantile', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.5)
    self.addLiteralInput(identifier = '-a', title = 'Do not align output with the input', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-c', title = 'Use circular neighborhood', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = 'grass_resolution_ns', title = 'Resolution of the mapset in north-south direction in meters or degrees', abstract = 'This parameter defines the north-south resolution of the mapset in meter or degrees, which should be used to process the input and output raster data. To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_resolution_ew', title = 'Resolution of the mapset in east-west direction in meters or degrees', abstract = 'This parameter defines the east-west resolution of the mapset in meters or degrees, which should be used to process the input and output raster data.  To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_band_number', title = 'Band to select for processing (default is all bands)', abstract = 'This parameter defines band number of the input raster files which should be processed. As default all bands are processed and used as single and multiple inputs for raster modules.', minOccurs = 0, maxOccurs = 1, type = type(0), allowedValues = '*')

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output raster map', formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("r.neighbors", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = r_neighbors()
  process.execute()
