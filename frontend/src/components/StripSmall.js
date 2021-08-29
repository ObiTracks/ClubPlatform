import React from 'react'

export default function StripSmall() {
    return (
        <a href="#">
            <div className="smallStrip">
                <div className="container">
                    <div className="header">
                        <div className="title">Title</div>
                        <div className="date-time">Date Time</div>
                    </div>
                    <div className="body paragraph_font">
                        Lorem ipsum dolor, sit amet consectetur adipisicing
                        elit. Lorem ipsum dolor, sit amet consectetur adipisicing
                        elit. Lorem ipsum dolor, sit amet consectetur adipisicing
                        elit. Lorem ipsum dolor, sit amet consectetur adipisicing
                        elit.
                    </div>
                </div>
                <img src="" alt="" className="thumbnail" />
            </div>
        </a>
    )
}
