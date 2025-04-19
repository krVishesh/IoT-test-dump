import gc

gc.collect()  # Run garbage collection first
print(f"Free memory before: {gc.mem_free()} bytes")

# Estimate memory usage of large objects
print(f"samples: {len(samples)} bytes")
print(f"converted_samples: {len(converted_samples)} bytes")
print(f"playback_samples: {len(playback_samples)} bytes")

gc.collect()
print(f"Free memory after: {gc.mem_free()} bytes")
