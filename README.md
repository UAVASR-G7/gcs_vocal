# gcs_vocal
Audio vocaliser for GCS

## Description
`gcs_vocal` is a simple ROS node designed for the UAVASR project. The node subscribes to various topics (see [Topics](#topics)) and when a message is received, an audible alert is made via the `espeak-ng` library.

### Topics
| Topic | Description | Message Type |
| --- | --- | --- |
| `vocal/aruco` | Triggered when the imagery subsystem detects an ArUCO marker | `std_msgs/Int32` |
| `vocal/land` | Triggered when the UAV lands at the end of the mission | `std_msgs/Bool` |
| `vocal/test` | Used to manually test that speaker is working (see [Testing](#testing)) | `std_msgs/String` |
| `target_detection/localisation` | Triggered when the imagery subsystem detects a target | `spar_msgs/TargetLocalisation` |

## Installation
1. Clone this repo into your catkin src directory.
```bash
git clone git@github.com:UAVASR-G7/gcs_vocal.git
```

2. Install addition dependencies. The `espeak` libraries required are not available via `rosdep` and must be installed manually using the following commands.
```bash
sudo apt-get install espeak-ng
```
```bash
pip install espeakng
```

3. Build the package.
```bash
catkin_make
```

## Testing
The vocalizer package can be tested using `rostopic pub` seen below.
```bash
rostopic pub /vocal/test std_msgs/String "Hello World"
```