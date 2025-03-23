
function convertImage() {
    const input = document.getElementById("imageInput");
    const format = document.getElementById("formatSelect").value;
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");

    if (input.files.length === 0) {
        alert("Please select an image to convert.");
        return;
    }

    const file = input.files[0];
    const reader = new FileReader();

    reader.onload = function (event) {
        const img = new Image();
        img.onload = function () {
            canvas.width = img.width;
            canvas.height = img.height;
            ctx.drawImage(img, 0, 0);

            const convertedImage = canvas.toDataURL(`image/${format}`);
            const downloadLink = document.getElementById("downloadLink");
            downloadLink.href = convertedImage;
            downloadLink.download = `converted_image.${format}`;
            downloadLink.style.display = "block";
            downloadLink.innerText = "Download Converted Image";
        };
        img.src = event.target.result;
    };

    reader.readAsDataURL(file);
}
