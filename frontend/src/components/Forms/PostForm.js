import React, { useState } from 'react'

export default function PostForm() {
    const [title, setTitle] = useState
    return (
        <form onSubmit={this.handleSubmit}>
            <label>Title: </label>
            <input type="text" value={this.state.value} onChange={this.handleChange} />

            <label>Description: </label>
            <textarea />

            <label>Long Description: </label>
            <textarea />

            <label>Date:</label>
            <input type="text" value={this.state.value} onChange={this.handleChange} />

            <label>Location:</label>
            <input type="text" value={this.state.value} onChange={this.handleChange} />

            <input type="submit" value="Submit" />
        </form>
    )
}
