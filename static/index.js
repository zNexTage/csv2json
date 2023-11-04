document.addEventListener("DOMContentLoaded", ()=>{
    const upload = document.getElementById("upload");

    upload.addEventListener("change", event => {
        const file = event.target.files[0];

        const filenameElement = document.getElementById("filename");

        filenameElement.innerHTML = `<br /> ${file.name}`;
    });    
});