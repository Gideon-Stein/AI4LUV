import replicate
import base64

path1 = "base_faces/D1.jpg"
binary_fc       = open("base_faces/D1.jpg", 'rb').read()  # fc aka file_content
base64_utf8_str = base64.b64encode(binary_fc).decode('utf-8')
ext     = path.split('.')[-1]
dataurl = f'data:image/{ext};base64,{base64_utf8_str}'

input = {
    "img": dataurl
}

output = replicate.run(
    "tencentarc/gfpgan:0fbacf7afc6c144e5be9767cff80f25aff23e52b0708f17e20f9879b2f21516c",
    input=input
)
with open(out_path, "wb") as file:
    file.write(output.read())



output = replicate.run(
    "cdingram/face-swap:d1d6ea8c8be89d664a07a457526f7128109dee7030fdac424788d762c71ed111",
    input={
        "swap_image": "base_faces/D1.jpg",
        "input_image": "https://replicate.delivery/pbxt/LPsGWYhFW03GN2y21RDRlat7YBCVPupkwyEg3Ca0YxcFWYNE/images.jpeg"
    }
)
print(output)