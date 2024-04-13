const URL='http://127.0.0.1:5000/color'

async function API_Call(){
    let response= await fetch(URL);
    let data= await response.json();
    
    data.forEach((i) => {
        console.log(i);
    });
}


API_Call();