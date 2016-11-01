import hashlib
import base64


def md5(filepath, blocksize=2**20):
    """
    Calculate the md5 hash for a file, streaming to limit memory usage.
    Returns a Base64-encoded string suitable for use with the Content-MD5 header
    as used by Amazon S3.
    """
    m = hashlib.md5()
    with open(filepath, "rb") as f:
        while True:
            block = f.read(blocksize)
            if not block:
                break
            m.update(block)
    return base64.b64encode(m.digest())
    # return m.hexdigest()  # <- like md5sum
