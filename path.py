import os

repo_path = R"C:\SSHS\codes\Projects\Rubix-cube"
checkpoint_path = os.getenv("APPDATA") + R"\Rubix-cube.ckpt"
save_path = FR"{repo_path}\ModelB.h5"
load_path = FR"{repo_path}\ModelA.h5"