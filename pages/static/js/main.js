    function toggle(tabName, tab2){

        if(tabName.classList.contains("hidden")){
            tabName.classList.remove("hidden")
            tab2.classList.add("hidden")
        }else{
            tabName.classList.add("hidden")
            tab2.classList.remove("hidden")
        }
    }

    
    not = document.getElementById("not")
    map = document.getElementById("map")
    notbtn = document.getElementById("notbtn")
    mapbtn = document.getElementById("mapbtn")

    function alert(){
        if(map.classList.contains("hidden")){
            val = 0
        }

        if(not.classList.contains("hidden")){
            not.classList.remove("hidden")
            map.classList.add("hidden")
        }
    }

    function maps(){
        if(not.classList.contains("hidden")){
            val = 0
        }

        if(map.classList.contains("hidden")){
            map.classList.remove("hidden")
            not.classList.add("hidden")
        }
    }

    mapbtn.onclick = maps
    notbtn.onclick = alert
