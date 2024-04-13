const URL='https://color-api-ng6n.onrender.com/color'

async function API_Call(){
    let response= await fetch(URL);
    let data= await response.json();
    
    data.forEach((i) => {
        console.log(i);
    });
}


API_Call();