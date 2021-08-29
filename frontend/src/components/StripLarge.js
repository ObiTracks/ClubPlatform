import React from 'react'
import Badge from './Badge';

export default function StripLarge() {
    return (
        <a href="#">
            <div className="largeStrip">
                <Badge />
                <div className="content">
                    <div className="container">
                        <div className="title">Title</div>
                        <div className="body paragraph_font_large">
                            Lorem ipsum, dolor sit amet consectetur adipisicing
                            elit. Cumque quo excepturi
                        </div>
                        <div className="details">Location Hybrid Meeting RSVPS</div>
                    </div>
                    <img src="" alt="" className="thumbnail" />
                </div>
            </div>
        </a>


    )
}
