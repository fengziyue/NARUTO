import numpy as np
import os

##################################################
### Scene specific parameters
##################################################
scene_name = "gZ6f7yhEvPG"
split_name = "tmp"
left_right = "left"
location_idx = 0

##################################################
### Directory
##################################################
dirs = dict(
    output_dir = "data/MP3D_sim/{}/{}/{}/{:02}".format(
                                            scene_name, 
                                            split_name,
                                            left_right,
                                            location_idx
                                            ),
    data_dir = "data/MP3D/v1/tasks/mp3d/{}".format(scene_name)
)

##################################################
### Simulator
##################################################
simulator = dict(
    physics = dict(
        enable = True,
        gravity = [0.0, -10.0, 0.0]
    ),
    scene_id = os.path.join(f"configs/MP3D/{scene_name}/mp3d.stage_config.json"),
    duration = 100, # sec
    FPS = 20,
)

##################################################
### Agent
##################################################
agent = dict(
    position = [0.0, 0.0, 0.0],
    rotation = [0.0, 0.0, 0.0],
    motion_profile = dict(
        radius = 1,
        motion_type = 'predefined', # [stationary, random, spiral_forward, spiral_forward_with_hori_rot, forward]
        predefined_traj_txt = "" # format of the pose: matrix as 16D vector. RDF c2w
    )
)

##################################################
### Camera
##################################################
### get FoV ###
fov = lambda size, focal: np.rad2deg(np.arctan((size/2)/focal))*2

camera = dict(
    fps = simulator['FPS'],
    pinhole = dict(
        enable = True,
        cam_type = ['color', 'depth'],
        resolution_hw = [680, 1200],
        orientation_type = 'horizontal', # [skybox, horizontal, horizontal+UpDown]
        horizontal = dict(
            num_rot = 1
        ),
        fov = (fov(680, 600), fov(1200, 600)), # h, w
    ),
    # DEBUG
    equirectangular = dict(
        enable = True,
        cam_type = ['color', 'depth'],
        resolution_hw = [1024, 2048],
        poses = [
            [0, 0, 0],
        ]
    ),
)

##################################################
### Simulation output storage
##################################################
sim_output = dict(
    save_video = True,
    save_frame = True,
    save_pose = True,
    save_K = True,
    frame_suffix = '.png',
    depth_png_scale = 6553.5,
    clear_old_output = True,
    force_clear = True, 
)

