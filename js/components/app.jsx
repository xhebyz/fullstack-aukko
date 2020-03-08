import React, {useState, useEffect} from 'react';
import Paper from '@material-ui/core/Paper';
import {makeStyles} from '@material-ui/core/styles';
import Select from '@material-ui/core/Select';
import MenuItem from '@material-ui/core/MenuItem';
import CustomizedTables from './table-data.jsx';
import {LinearProgress} from '@material-ui/core';
import Button from '@material-ui/core/Button';

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
    const [category, setCategory] = useState('-1');
    const [books, setBooks] = useState([]);
    const [loading, setLoading] = useState(true);
    const [categoryName, setCategoryName] = useState('');

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
                setCategoryName(category_data.name);
                setBooks(category_data.books);
                setLoading(false)
            });
    }


    const launchScraping = () => {
        setLoading(true)
        fetch(`/api/v1/scraping`)
            .then(result => {
                return result.json();
            })
            .then(response => {
                setLoading(false)
            }).catch(err => {
            setLoading(false)

        });
    }


    const handleChange = event => {
        let categories_id = event.target.value
        setCategory(categories_id);
        let category_data = categories[categories_id];
        console.log(category_data.books)
        setBooks(category_data.books);
        setCategoryName(category_data.name);
    };

    return (

        <div style={{margin: '0 auto'}}>
            {loading && <LinearProgress/>}

            <Paper style={{textAlign: 'center'}}>

                <div style={{padding: '10px'}}>
                    <Button onClick={launchScraping} variant="contained" color="primary" style={{marginRight: '25px'}}>Scraping
                        Book</Button>
                    <Select
                        value={category}
                        onChange={handleChange}
                    >

                        <MenuItem value='-1'>Select Category</MenuItem>

                        {
                            categories.map((cat, i) => {
                                console.log("Entered");
                                // Return the element. Also pass key
                                return (
                                    <MenuItem value={i}>{cat.name}</MenuItem>
                                )
                            })
                        }
                    </Select>
                </div>
                <CustomizedTables data={books} setBooks={setBooksHandle} categoryName={categoryName}/>
            </Paper>
        </div>
    );
}