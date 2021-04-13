const Swal = require('sweetalert2')

function detectFaces() {
  const btn = document.getElementById("detect");
  btn.innerText = "Loading...";
  btn.disabled = true;
  var {PythonShell} = require("python-shell");
  var path = require("path");

  var options = {
    scriptPath: path.join(__dirname, "/../engine/face_recognition/"),
  };

  var face = new PythonShell("detect_faces.py", options);

  face.end(function (err, code, message) {
    btn.innerText = "Detect faces";
    btn.disabled = false;
  });
}

function addFace() {
  const btn = document.getElementById("add");
  const {PythonShell} = require("python-shell");
  const path = require("path");
  const input = document.getElementById("person");
  const name = input.value;
  
  btn.innerText = "Loading...";
  btn.disabled = true;

  var options = {
    scriptPath: path.join(__dirname, "/../engine/face_recognition/"),
    args: ["cam", name],
  };
  if(!name) {
    swal("Please provide your Name", '', "error");
    btn.innerText = "Add a new face";
    btn.disabled = false;
    return;
  }
  var face = new PythonShell("add_face.py", options);

  face.end(function (err, code, message) {
    console.log(err, code, message);
    btn.innerText = "Add a new face";
    btn.disabled = false;
    input.value = '';
    swal("Face added!", `We can now recognize your face ${name}`, "success");
  });
}

function startJob() {
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
          Swal.fire({
            icon: 'info',
            title: 'Supervising was successfully stopped!'
          })
          return;
        }

        const teamShot = new PythonShell("take_first_snap.py", options);
    
        teamShot.end(function (err, code, message) {
            Swal.fire({
                icon: 'success',
                title: 'The screenshot has been taken successfully!',
                html: 'The every 10s job has been started successfully!',
                width: '50rem',
                confirmButtonText: 'Ok',
                timer: 3000
            })

            const nextShots = new PythonShell("take_next_snaps.py", options);
            
            nextShots.end(function (err, code, message) {
                console.log(err, code, message);
                Swal.fire({
                    title: 'The job was stopped!',
                    icon: 'error',
                    width: '50rem',
                    confirmButtonText: 'Ok'
                })
            });
        })
    })
}
