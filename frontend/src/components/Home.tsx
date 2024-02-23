import {useState,useEffect} from "react"
import {getCSRFToken,getSessionId } from "../utils/GetAuth"

function Home(){
    const URL = import.meta.env.VITE_API_URL
    const [isLogIn,setIsLogIn] = useState(false)
    async function getHomePageData(){
        try{
            const response = await fetch(URL+"",{
                method : "GET",
                headers : {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${getSessionId()}`, 
                    'X-CSRFToken': `${getCSRFToken()}`,  
                },
            })
            if (response.redirected) {
                // You can access the redirected URL using response.url
                console.log("Redirecting")
                window.location.href = response.url;
              } else {
                // Handle the JSON response
                const data = await response.json()
                console.log(data)
                setIsLogIn(true)
                return response.json();
              }
            
        }catch(e){
            console.log(e)
        }
    }
    useEffect(()=>{
        console.log(getCSRFToken())
        console.log(getSessionId())
        getHomePageData()
    },[])
    if(isLogIn){
        return <div>
            <h2>Home</h2>
        </div>
    }
    
}

export default Home