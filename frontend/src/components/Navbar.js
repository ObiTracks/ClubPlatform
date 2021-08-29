import React from 'react'
import ProfileTab from './ProfileTab'

export default function Navbar() {
    return (
        <div class="navbar">
            <div></div>
            <div>
                <input type="text" id="s-bar" name="searchbar" class="searchbar" placeholder="Search here" />
            </div>
            <div>
                <ProfileTab />
            </div>
        </div>
    )
}
