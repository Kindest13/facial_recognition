const Swal = require('sweetalert2')

function validateEmail(email) {
  const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(String(email).toLowerCase());
}

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
    const {PythonShell} = require("python-shell");
    const path = require("path");
    let timerInterval;
    let mail;
  
    const options = {
      scriptPath: path.join(__dirname, "/../engine/"),
    };
    Swal.fire({
      title: 'Please provide your email',
      input: 'text',
      inputAttributes: {
        autocapitalize: 'off'
      },
      showDenyButton: true,
      confirmButtonText: 'Set and Start',
      denyButtonText: 'Cancel',
      preConfirm: (email) => {
        mail = email;
        console.log(mail)
      },
      inputValidator: (value) => {
        return !validateEmail(value) && 'Provide valid email. Example: bla@mail.com'
      }
    }, 'success').then((result) => {
      if(result.isDenied) {
        return false;
      }

      Swal.fire({
        title: 'The screenshot will be taken in&nbsp;<strong></strong>&nbsp;seconds.',
        text: 'Please open your videochat tab.',
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

        const options2 = {
          scriptPath: path.join(__dirname, "/../engine/"),
          args: [mail]
        };
    
        teamShot.end(function (err, code, message) {
            Swal.fire({
                icon: 'success',
                title: 'The screenshot has been taken successfully!',
                text: 'The every 10s job has been started successfully!',
                width: '50rem',
                confirmButtonText: 'Ok',
                timer: 3000
            })

            const nextShots = new PythonShell("take_next_snaps.py", options2);

            nextShots.end(function (err, code, message) {
                console.log(err, code, message);
                Swal.fire({
                    title: 'The job was stopped!',
                    icon: 'error',
                    confirmButtonText: 'Ok'
                })
            });
        })
    })
})}
