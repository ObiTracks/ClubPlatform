import React from 'react'

export default function Menu() {
    return (
        <div className="menu">
            <div className="buttonsPanel">
                <button className="icon icon-1" onclick="showMenu()">
                    <img src="" alt="" />
                </button>
                <button className="icon icon-2">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                        <path d="M24 10h-10v-10h-4v10h-10v4h10v10h4v-10h10z" />
                    </svg>
                </button>
            </div>
            <div className="menuPanel" id="Menu">
                <button className="menu-bucket menu-bucket-active">
                    <img src="" alt="" className="bucket-icon" />
                    <div className="title">Bucket Name</div>
                    <img src="" alt="" className="action-symbol" />
                </button>
                <button className="menu-bucket menu-bucket-inactive">
                    <img src="" alt="" className="bucket-icon" />
                    <div className="title">Bucket Name</div>
                    <img src="" alt="" className="action-symbol" />
                </button>
            </div>
        </div>
    )
}

function showMenu() {
    console.log("Button pressed");
    var menu = document.getElementById("Menu");

    if (menu.style.opacity == 0) {
        menu.style.opacity = 1;
        menu.style.display = "flex";
    } else {
        menu.style.opacity = 0;
        menu.style.display = "none";
    }
}