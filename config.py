# import argparse

# def agr():
#     parser = argparse.ArgumentParser(
#         description="Inspired by MaskTheFace - Python code to mask faces dataset"
#     )
# 
#     parser.add_argument(
#         "--path",
#         type=str,
#         default="",
#         help="Path to either the folder containing images or the image itself",
#     )
#     parser.add_argument(
#         "--mask_type",
#         type=str,
#         default="random",
#         choices=["surgical", "N95", "KN95", "cloth", "gas", "inpaint", "random", "all"],
#         help="Type of the mask to be applied. Available options: all, surgical_blue, surgical_green, N95, cloth",
#     )
#     parser.add_argument(
#         "--pattern",
#         type=str,
#         default="",
#         help="Type of the pattern. Available options in masks/textures",
#     )
#     parser.add_argument(
#         "--pattern_weight",
#         type=float,
#         default=0.5,
#         help="Weight of the pattern. Must be between 0 and 1",
#     )
#     parser.add_argument(
#         "--color",
#         type=bool,
#         default=True,
#         help="if true, overlayed a random color to the mask",
#     )
#     parser.add_argument(
#         "--color_weight",
#         type=float,
#         default=0.5,
#         help="Weight of the color intensity. Must be between 0 and 1",
#     )
#     parser.add_argument(
#         "--code",
#         type=str,
#         default="",
#         help="Generate specific formats",
#     )
#     parser.add_argument(
#         "--verbose", dest="verbose", action="store_true", help="Turn verbosity on"
#     )
#     parser.add_argument(
#         "--write_original_image",
#         dest="write_original_image",
#         action="store_true",
#         help="If true, original image is also stored in the masked folder",
#     )
#     parser.set_defaults(feature=False)
#     args = parser.parse_args()
#     args.write_path = args.path + "_masked"
#     return args
# 
mask_type = 'random'  # choices=["surgical", "N95", "KN95", "cloth", "inpaint", "random"]
color = True
color_weight = 0.3
code = ''
write_original_image = ''
maskconfig_path = 'mask_module/masks/masks.cfg'
pattern = False
pattern_weight = False
