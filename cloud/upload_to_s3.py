"""
Upload vers Amazon S3
---------------------
Envoie la vidéo traitée vers le stockage cloud.
"""

import boto3

s3 = boto3.client("s3")

BUCKET_NAME = "videop-bucket"
FILE_PATH = "/data/downscaled/video_downscaled.mp4"
S3_KEY = "videos/video.mp4"

s3.upload_file(FILE_PATH, BUCKET_NAME, S3_KEY)

print("✅ Upload vers S3 terminé")

