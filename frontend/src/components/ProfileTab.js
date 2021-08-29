import React from 'react'

export default function ProfileTab() {
    return (
        <button className="profileTab">
            <img src="" alt="" />
            <div className="body">
                <div className="name">Person Name</div>
                <svg className="icon" xmlns="http://www.w3.org/2000/svg" width="10" height="10" viewBox="0 0 24 24">
                    <path d="M0 7.33l2.829-2.83 9.175 9.339 9.167-9.339 2.829 2.83-11.996 12.17z" />
                </svg>
                <div id="position">Role</div>
            </div>
        </button>
    )
}
