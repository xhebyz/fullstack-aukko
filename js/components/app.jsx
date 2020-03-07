import React, {useState, useEffect} from 'react';
import Paper from '@material-ui/core/Paper';
import {makeStyles} from '@material-ui/core/styles';
import Select from '@material-ui/core/Select';
import MenuItem from '@material-ui/core/MenuItem';
import CustomizedTables from './table-data.jsx';
import {LinearProgress} from '@material-ui/core';

const useStyles = makeStyles(theme => ({
    rounded: {
        color: '#fff',
        backgroundColor: '#1BB3A6',
    },
    center: {
        marginLeft: 'auto',
        marginRight: 'auto',
        justifyContent: 'center',
        display: 'flex',
        '& > *': {
            margin: theme.spacing(1),
        }
    }
}));

export default function App() {
    const classes = useStyles();
    const [categories, setCategories] = useState([]);
    const [category, setCategory] = useState(0);
    const [books, setBooks] = useState([]);
    const [loading, setLoading] = useState(true);
    const [booksSize, setBookSize] = useState(0);

    if (categories.length == 0) {
        fetch(`/api/v1/categories`)
            .then(result => {
                return result.json();
            })
            .then(response => {
                console.log(response)
                setCategories(response.categories);
                setLoading(false)
            });
    }

    const setBooksHandle = (books) => {
        setLoading(true)
        fetch(`/api/v1/categories`)
            .then(result => {
                return result.json();
            })
            .then(response => {
                console.log(response)
                setCategories(response.categories);
                let category_data = categories[category];
                setBooks(category_data.books);
                setLoading(false)
            });
    }

    const handleChange = event => {
        let categories_id = event.target.value
        setCategory(categories_id);
        let category_data = categories[categories_id];
        console.log(category_data.books)
        setBooks(category_data.books);
        setBookSize(category_data.books.length)
    };
    return (

        <div style={{maxWidth: '900px', margin: '0 auto'}}>
            {loading && <LinearProgress/>}

            <Paper style={{textAlign: 'center'}}>


                <Select
                    value={category}
                    onChange={handleChange}
                >
                    {
                        categories.map((cat, i) => {
                            console.log("Entered");
                            // Return the element. Also pass key
                            return (
                                <MenuItem value={cat.id}>{cat.name}</MenuItem>
                            )
                        })
                    }
                </Select>
                <CustomizedTables data={books} setBooks={setBooksHandle}/>
            </Paper>
        </div>
    );
}