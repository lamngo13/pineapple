import os, time 
bruh = "{'audio_features': [{'danceability': 0.543, 'energy': 0.974, 'key': 0, 'loudness': -6.525, 'mode': 1, 'speechiness': 0.0639, 'acousticness': 0.000735, 'instrumentalness': 0.92, 'liveness': 0.219, 'valence': 0.463, 'tempo': 170.001, 'type': 'audio_features', 'id': '17vJ4JDM5nsU4jxZgl1QSR', 'uri': 'spotify:track:17vJ4JDM5nsU4jxZgl1QSR', 'track_href': 'https://api.spotify.com/v1/tracks/17vJ4JDM5nsU4jxZgl1QSR', 'analysis_url': 'https://api.spotify.com/v1/audio-analysis/17vJ4JDM5nsU4jxZgl1QSR', 'duration_ms': 196235, 'time_signature': 4}, {'danceability': 0.671, 'energy': 0.73, 'key': 7, 'loudness': -7.189, 'mode': 1, 'speechiness': 0.29, 'acousticness': 0.414, 'instrumentalness': 0, 'liveness': 0.107, 'valence': 0.248, 'tempo': 99.971, 'type': 'audio_features', 'id': '3pzkWSjCdHKdzNEljKI4gz', 'uri': 'spotify:track:3pzkWSjCdHKdzNEljKI4gz', 'track_href': 'https://api.spotify.com/v1/tracks/3pzkWSjCdHKdzNEljKI4gz', 'analysis_url': 'https://api.spotify.com/v1/audio-analysis/3pzkWSjCdHKdzNEljKI4gz', 'duration_ms': 160800, 'time_signature': 4}, {'danceability': 0.767, 'energy': 0.444, 'key': 3, 'loudness': -13.671, 'mode': 1, 'speechiness': 0.557, 'acousticness': 0.941, 'instrumentalness': 0.000236, 'liveness': 0.144, 'valence': 0.527, 'tempo': 80.181, 'type': 'audio_features', 'id': '7i6jHKsAShYpPTN4kS4WBW', 'uri': 'spotify:track:7i6jHKsAShYpPTN4kS4WBW', 'track_href': 'https://api.spotify.com/v1/tracks/7i6jHKsAShYpPTN4kS4WBW', 'analysis_url': 'https://api.spotify.com/v1/audio-analysis/7i6jHKsAShYpPTN4kS4WBW', 'duration_ms': 168066, 'time_signature': 4}, {'danceability': 0.858, 'energy': 0.339, 'key': 10, 'loudness': -15.847, 'mode': 0, 'speechiness': 0.0808, 'acousticness': 0.0558, 'instrumentalness': 0.297, 'liveness': 0.119, 'valence': 0.194, 'tempo': 158.968, 'type': 'audio_features', 'id': '1Bt9doNZTAw34cuW2FxaZW', 'uri': 'spotify:track:1Bt9doNZTAw34cuW2FxaZW', 'track_href': 'https://api.spotify.com/v1/tracks/1Bt9doNZTAw34cuW2FxaZW', 'analysis_url': 'https://api.spotify.com/v1/audio-analysis/1Bt9doNZTAw34cuW2FxaZW', 'duration_ms': 193242, 'time_signature': 4}, {'danceability': 0.794, 'energy': 0.258, 'key': 8, 'loudness': -17.258, 'mode': 0, 'speechiness': 0.432, 'acousticness': 0.456, 'instrumentalness': 1.15e-05, 'liveness': 0.0848, 'valence': 0.393, 'tempo': 50.047, 'type': 'audio_features', 'id': '6BjmeqZw3N9etV8Oa2CkH1', 'uri': 'spotify:track:6BjmeqZw3N9etV8Oa2CkH1', 'track_href': 'https://api.spotify.com/v1/tracks/6BjmeqZw3N9etV8Oa2CkH1', 'analysis_url': 'https://api.spotify.com/v1/audio-analysis/6BjmeqZw3N9etV8Oa2CkH1', 'duration_ms': 71444, 'time_signature': 4}, {'danceability': 0.561, 'energy': 0.402, 'key': 4, 'loudness': -13.542, 'mode': 0, 'speechiness': 0.493, 'acousticness': 0.624, 'instrumentalness': 0, 'liveness': 0.324, 'valence': 0.371, 'tempo': 129.365, 'type': 'audio_features', 'id': '57wZV2CA5dbaJqyxxYUfK2', 'uri': 'spotify:track:57wZV2CA5dbaJqyxxYUfK2', 'track_href': 'https://api.spotify.com/v1/tracks/57wZV2CA5dbaJqyxxYUfK2', 'analysis_url': 'https://api.spotify.com/v1/audio-analysis/57wZV2CA5dbaJqyxxYUfK2', 'duration_ms': 105579, 'time_signature': 4}, {'danceability': 0.908, 'energy': 0.19, 'key': 7, 'loudness': -16.072, 'mode': 0, 'speechiness': 0.772, 'acousticness': 0.14, 'instrumentalness': 0, 'liveness': 0.108, 'valence': 0.18, 'tempo': 129.872, 'type': 'audio_features', 'id': '5MuiMQ0ZTtGbVNRLBynOeE', 'uri': 'spotify:track:5MuiMQ0ZTtGbVNRLBynOeE', 'track_href': 'https://api.spotify.com/v1/tracks/5MuiMQ0ZTtGbVNRLBynOeE', 'analysis_url': 'https://api.spotify.com/v1/audio-analysis/5MuiMQ0ZTtGbVNRLBynOeE', 'duration_ms': 147767, 'time_signature': 4}, {'danceability': 0.87, 'energy': 0.376, 'key': 8, 'loudness': -12.932, 'mode': 0, 'speechiness': 0.358, 'acousticness': 0.888, 'instrumentalness': 1.94e-06, 'liveness': 0.137, 'valence': 0.387, 'tempo': 121.02, 'type': 'audio_features', 'id': '4QhPHgDgAFbbrWS7bcpEoj', 'uri': 'spotify:track:4QhPHgDgAFbbrWS7bcpEoj', 'track_href': 'https://api.spotify.com/v1/tracks/4QhPHgDgAFbbrWS7bcpEoj', 'analysis_url': 'https://api.spotify.com/v1/audio-analysis/4QhPHgDgAFbbrWS7bcpEoj', 'duration_ms': 178512, 'time_signature': 4}, {'danceability': 0.517, 'energy': 0.601, 'key': 5, 'loudness': -13.415, 'mode': 1, 'speechiness': 0.736, 'acousticness': 0.223, 'instrumentalness': 0, 'liveness': 0.0598, 'valence': 0.731, 'tempo': 148.334, 'type': 'audio_features', 'id': '3fYVwsvmV4QRhLVZcuL5yy', 'uri': 'spotify:track:3fYVwsvmV4QRhLVZcuL5yy', 'track_href': 'https://api.spotify.com/v1/tracks/3fYVwsvmV4QRhLVZcuL5yy', 'analysis_url': 'https://api.spotify.com/v1/audio-analysis/3fYVwsvmV4QRhLVZcuL5yy', 'duration_ms': 139829, 'time_signature': 4}, {'danceability': 0.831, 'energy': 0.532, 'key': 11, 'loudness': -4.941, 'mode': 0, 'speechiness': 0.278, 'acousticness': 0.158, 'instrumentalness': 1.23e-06, 'liveness': 0.656, 'valence': 0.506, 'tempo': 112.929, 'type': 'audio_features', 'id': '3xls9xAVcGhHqc5B7e8Ywa', 'uri': 'spotify:track:3xls9xAVcGhHqc5B7e8Ywa', 'track_href': 'https://api.spotify.com/v1/tracks/3xls9xAVcGhHqc5B7e8Ywa', 'analysis_url': 'https://api.spotify.com/v1/audio-analysis/3xls9xAVcGhHqc5B7e8Ywa', 'duration_ms': 255216, 'time_signature': 4}, {'danceability': 0.759, 'energy': 0.417, 'key': 1, 'loudness': -14.489, 'mode': 1, 'speechiness': 0.502, 'acousticness': 0.0147, 'instrumentalness': 1.01e-05, 'liveness': 0.171, 'valence': 0.401, 'tempo': 86.016, 'type': 'audio_features', 'id': '755l4UkvolIqUBjlsv6uID', 'uri': 'spotify:track:755l4UkvolIqUBjlsv6uID', 'track_href': 'https://api.spotify.com/v1/tracks/755l4UkvolIqUBjlsv6uID', 'analysis_url': 'https://api.spotify.com/v1/audio-analysis/755l4UkvolIqUBjlsv6uID', 'duration_ms': 120000, 'time_signature': 4}, {'danceability': 0.869, 'energy': 0.37, 'key': 8, 'loudness': -13.299, 'mode': 0, 'speechiness': 0.331, 'acousticness': 0.87, 'instrumentalness': 1.92e-06, 'liveness': 0.137, 'valence': 0.392, 'tempo': 120.956, 'type': 'audio_features', 'id': '2liy0NM9d6CjAx3EwWksyN', 'uri': 'spotify:track:2liy0NM9d6CjAx3EwWksyN', 'track_href': 'https://api.spotify.com/v1/tracks/2liy0NM9d6CjAx3EwWksyN', 'analysis_url': 'https://api.spotify.com/v1/audio-analysis/2liy0NM9d6CjAx3EwWksyN', 'duration_ms': 178512, 'time_signature': 4}, {'danceability': 0.533, 'energy': 0.562, 'key': 4, 'loudness': -14.524, 'mode': 0, 'speechiness': 0.649, 'acousticness': 0.02, 'instrumentalness': 0, 'liveness': 0.307, 'valence': 0.4, 'tempo': 137.653, 'type': 'audio_features', 'id': '2mrwdu7Cdezo4xOGEni7Rv', 'uri': 'spotify:track:2mrwdu7Cdezo4xOGEni7Rv', 'track_href': 'https://api.spotify.com/v1/tracks/2mrwdu7Cdezo4xOGEni7Rv', 'analysis_url': 'https://api.spotify.com/v1/audio-analysis/2mrwdu7Cdezo4xOGEni7Rv', 'duration_ms': 185977, 'time_signature': 4}, {'danceability': 0.673, 'energy': 0.533, 'key': 9, 'loudness': -14.668, 'mode': 1, 'speechiness': 0.0881, 'acousticness': 0.245, 'instrumentalness': 0.000569, 'liveness': 0.0719, 'valence': 0.21, 'tempo': 75.099, 'type': 'audio_features', 'id': '3elRCrT4kWcVyP2EjPc8cP', 'uri': 'spotify:track:3elRCrT4kWcVyP2EjPc8cP', 'track_href': 'https://api.spotify.com/v1/tracks/3elRCrT4kWcVyP2EjPc8cP', 'analysis_url': 'https://api.spotify.com/v1/audio-analysis/3elRCrT4kWcVyP2EjPc8cP', 'duration_ms': 275017, 'time_signature': 4}, {'danceability': 0.701, 'energy': 0.389, 'key': 11, 'loudness': -15.256, 'mode': 0, 'speechiness': 0.393, 'acousticness': 0.0701, 'instrumentalness': 0.000837, 'liveness': 0.233, 'valence': 0.0683, 'tempo': 101.533, 'type': 'audio_features', 'id': '1t7sVX8wCMVZHFSfYH2Y0y', 'uri': 'spotify:track:1t7sVX8wCMVZHFSfYH2Y0y', 'track_href': 'https://api.spotify.com/v1/tracks/1t7sVX8wCMVZHFSfYH2Y0y', 'analysis_url': 'https://api.spotify.com/v1/audio-analysis/1t7sVX8wCMVZHFSfYH2Y0y', 'duration_ms': 107500, 'time_signature': 4}, {'danceability': 0.682, 'energy': 0.37, 'key': 11, 'loudness': -16.388, 'mode': 0, 'speechiness': 0.228, 'acousticness': 0.0557, 'instrumentalness': 0, 'liveness': 0.0805, 'valence': 0.356, 'tempo': 137.137, 'type': 'audio_features', 'id': '3xNTYCJki80XXOphZi7UKu', 'uri': 'spotify:track:3xNTYCJki80XXOphZi7UKu', 'track_href': 'https://api.spotify.com/v1/tracks/3xNTYCJki80XXOphZi7UKu', 'analysis_url': 'https://api.spotify.com/v1/audio-analysis/3xNTYCJki80XXOphZi7UKu', 'duration_ms': 117295, 'time_signature': 4}, {'danceability': 0.425, 'energy': 0.325, 'key': 9, 'loudness': -10.221, 'mode': 1, 'speechiness': 0.045, 'acousticness': 0.538, 'instrumentalness': 0, 'liveness': 0.622, 'valence': 0.0654, 'tempo': 108.605, 'type': 'audio_features', 'id': '5PNmwrKFzYrEv5jhgCjxhs', 'uri': 'spotify:track:5PNmwrKFzYrEv5jhgCjxhs', 'track_href': 'https://api.spotify.com/v1/tracks/5PNmwrKFzYrEv5jhgCjxhs', 'analysis_url': 'https://api.spotify.com/v1/audio-analysis/5PNmwrKFzYrEv5jhgCjxhs', 'duration_ms': 142307, 'time_signature': 4}, {'danceability': 0.373, 'energy': 0.362, 'key': 11, 'loudness': -12.048, 'mode': 1, 'speechiness': 0.0288, 'acousticness': 0.0267, 'instrumentalness': 0.862, 'liveness': 0.0866, 'valence': 0.416, 'tempo': 179.956, 'type': 'audio_features', 'id': '3Kpsnwm3geSUFyQDBc7Rgw', 'uri': 'spotify:track:3Kpsnwm3geSUFyQDBc7Rgw', 'track_href': 'https://api.spotify.com/v1/tracks/3Kpsnwm3geSUFyQDBc7Rgw', 'analysis_url': 'https://api.spotify.com/v1/audio-analysis/3Kpsnwm3geSUFyQDBc7Rgw', 'duration_ms': 108267, 'time_signature': 4}, {'danceability': 0.72, 'energy': 0.679, 'key': 6, 'loudness': -8.782, 'mode': 0, 'speechiness': 0.0456, 'acousticness': 0.0604, 'instrumentalness': 0.552, 'liveness': 0.165, 'valence': 0.889, 'tempo': 121.245, 'type': 'audio_features', 'id': '3ezhOp8Loy3SpY7mJqZuer', 'uri': 'spotify:track:3ezhOp8Loy3SpY7mJqZuer', 'track_href': 'https://api.spotify.com/v1/tracks/3ezhOp8Loy3SpY7mJqZuer', 'analysis_url': 'https://api.spotify.com/v1/audio-analysis/3ezhOp8Loy3SpY7mJqZuer', 'duration_ms': 343880, 'time_signature': 4}, {'danceability': 0.516, 'energy': 0.761, 'key': 4, 'loudness': -8.721, 'mode': 0, 'speechiness': 0.0579, 'acousticness': 0.0066, 'instrumentalness': 0.0895, 'liveness': 0.338, 'valence': 0.301, 'tempo': 119.597, 'type': 'audio_features', 'id': '4fFpJhPFy9Vmm8Oc4Ygams', 'uri': 'spotify:track:4fFpJhPFy9Vmm8Oc4Ygams', 'track_href': 'https://api.spotify.com/v1/tracks/4fFpJhPFy9Vmm8Oc4Ygams', 'analysis_url': 'https://api.spotify.com/v1/audio-analysis/4fFpJhPFy9Vmm8Oc4Ygams', 'duration_ms': 262347, 'time_signature': 4}]}"

bruh = bruh.replace('\'danceability\'', '\'genre\': Rap, \'danceability\'')

file = open("rap2.txt", "a")
file.write(bruh)
