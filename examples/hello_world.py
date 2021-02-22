import json
import asf_search as asf

# Using constants
print(f'asf.DATASET.AVNIR: {asf.DATASET.AVNIR}')
print(f'asf.BEAMMODE.IW: {asf.BEAMMODE.IW}')
print(f'asf.POLARIZATION.HH_HV: {asf.POLARIZATION.HH_HV}')
print(f'asf.PLATFORM.SENTINEL1: {asf.PLATFORM.SENTINEL1}')
print(f'Health check: {json.dumps(asf.health(), indent=2)}')

# Checking health
results = asf.search(platform='S1', maxresults=2)
print(f'Basic search check: {json.dumps(results, indent=2)}')

# Granule list searches
results = asf.granule_search('ALPSRS279162400')
print(f'Granule search check: {json.dumps(results, indent=2)}')
results = asf.granule_search(['ALPSRS279162400','ALPSRS279162200'])
print(f'Granule search check: {json.dumps(results, indent=2)}')

# Product list searches
results = asf.product_search('ALAV2A279152900')
print(f'Product search check: {json.dumps(results, indent=2)}')
results = asf.product_search(['ALAV2A279102730','ALAV2A279133150'])
print(f'Product search check: {json.dumps(results, indent=2)}')

# Alternate SearchAPI maturities
results = asf.search(platform='S1', maxresults=2, host=asf.INTERNAL.HOST_TEST)
print(f'Basic search check: {json.dumps(results, indent=2)}')