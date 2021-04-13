const Swal = require('sweetalert2')

function detect_faces() {
  document.getElementById("detect").value = "Hang on...";
  var {PythonShell} = require("python-shell");
  var path = require("path");

  var options = {
    scriptPath: path.join(__dirname, "/../engine/face_recognition/"),
  };

  var face = new PythonShell("detect_faces.py", options);

  face.end(function (err, code, message) {
    document.getElementById("detect").value = "Detect faces";
  });
}

function add_face() {
  var {PythonShell} = require("python-shell");
  var path = require("path");
  var name = document.getElementById("person").value;
  console.log(name)

  var options = {
    scriptPath: path.join(__dirname, "/../engine/face_recognition/"),
    args: ["cam", name],
  };

  var face = new PythonShell("add_face.py", options);

  face.end(function (err, code, message) {
    console.log(err, code, message);
    swal("Face added!", "We can now recognize your face", "success");
    // document.getElementsById("add").innerHTML = "Add a new face";
  });
}

function start_job() {
    var {PythonShell} = require("python-shell");
    var path = require("path");
    let timerInterval;
  
    var options = {
      scriptPath: path.join(__dirname, "/../engine/"),
    };
    Swal.fire({
        title: 'The screenshot will be taken in&nbsp;<strong></strong>&nbsp;seconds.',
        html: 'Please open your videochat tab.',
        showDenyButton: true,
        width: '50rem',
        confirmButtonText: 'Ok',
        denyButtonText: 'Cancel job',
        timer: 5000,
        willOpen: () => {
            timerInterval = setInterval(() => {
              Swal.getTitle().querySelector('strong')
                .textContent = (Swal.getTimerLeft() / 1000)
                  .toFixed(0)
            }, 100)
        },
        willClose: () => {
          clearInterval(timerInterval)
        }
      }, 'success').then((result) => {
        if (result.isDenied) {
          Swal.fire('Supervising job was successfully stopped', '', 'info')
          return;
        }

        const team_shot = new PythonShell("take_first_snap.py", options);
    
        team_shot.end(function (err, code, message) {
            console.log(err, code, message);
            Swal.fire({
                title: 'The screenshot has been taken successfully!',
                html: 'The every 10s job has been started successfully!',
                width: '50rem',
                confirmButtonText: 'Ok',
                timer: 3000
            })

            const next_shots = new PythonShell("take_next_snaps.py", options);
            
            next_shots.end(function (err, code, message) {
                console.log(err, code, message);
                Swal.fire({
                    title: 'The job was stopped!',
                    type: 'error',
                    width: '50rem',
                    confirmButtonText: 'Ok'
                })
            });
        })
    })
}
