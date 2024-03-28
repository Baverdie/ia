from google_images_download import google_images_download

image_dir = "./dataset"
response = google_images_download.googleimagesdownload()

arguments = [
	{
		"keywords": "dog",
		"limit": 10,
		"print_urls": True,
		"output_directory": image_dir
	},
	{
		"keywords": "cat",
		"limit": 10,
		"print_urls": True,
		"output_directory": image_dir
	}
]

for arg in arguments:
	paths = response.download(arg)

print(paths)