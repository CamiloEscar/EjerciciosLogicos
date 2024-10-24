

const apikey = 'dTVOOHuMdTNXXlix9ZTOcxzcOLneLtxX'

const peticion = fetch(`http://api.giphy.com/v1/gifs/random?api_key=${apikey}`)


peticion
// esto se conoce como promesa en cadena
    .then(resp => resp.json() )
    .then( ({ data }) => {
        const { url } = data.images.original
        
        const img = document.createElement('img');
        img.src = url;

        document.body.append(img);
    })

    .catch(console.warn);

