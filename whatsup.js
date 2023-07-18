const qrcode = require('qrcode-terminal');
const fs = require('fs');
const path = require('path');

const { Client } = require('whatsapp-web.js');
const client = new Client();

client.on('qr', qr => {
    qrcode.generate(qr, {small: true});
});

client.on('ready', () => {
    console.log('Client is ready!');
    client.on('message', async msg => {
         if(msg.hasMedia) {
            const media = await msg.downloadMedia();
            const mimetype = media.mimetype;

            if (mimetype === 'image/png') {
              // Reply with a message saying that the image is a PNG.
              msg.reply('Thanku for shareing your file, here you will find summary of your file.');
              msg.reply('https://drive.google.com/drive/folders/12UAmlWFiLxIsaiWga_Zgj4hIPp5DVbgb?usp=sharing');
            } else if (mimetype === 'image/jpeg') {
              // Reply with a message saying that the image is a JPEG.
              msg.reply('Thanku for shareing your file, here you will find summary of your file.');
              msg.reply('https://drive.google.com/drive/folders/12UAmlWFiLxIsaiWga_Zgj4hIPp5DVbgb?usp=sharing');
            }
            // do something with the media data here
            function convertAndSaveImage(base64Data, outputPath) {
                const imageData = base64Data.replace(/^data:image\/\w+;base64,/, '');
                const buffer = Buffer.from(imageData, 'base64');
              
                fs.writeFile(outputPath, buffer, (error) => {
                  if (error) {
                    console.error('Error saving the image:', error);
                  } else {
                    console.log('Image saved successfully:', outputPath);
                  }
                });
              }
              
              const outputFolder = './upload';
              const outputFilename = `image_${Date.now()}.jpg`;
              const outputPath = path.join(outputFolder, outputFilename);

              
              fs.mkdirSync(outputFolder, { recursive: true }); // Create the output folder if it doesn't exist
              
              convertAndSaveImage(media.data, outputPath);
            console.log(media)
        }
    });
});

client.initialize();