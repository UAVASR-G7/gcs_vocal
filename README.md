# gcs_vocal
Audio vocaliser for GCS

## Testing
The vocalizer package can be tested using `rostopic pub` seen below.
```bash
rostopic pub /vocal/test std_msgs/String "Hello World"
```

## Additional Dependencies
The `espeak` libraries required are not available via `rosdep` and must be installed manually using the following commands.
```bash
sudo apt-get install espeak-ng
```
```bash
pip install espeakng
```
