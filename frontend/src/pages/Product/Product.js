import React, { useEffect, useState } from "react";
import {
    Container,
    Card,
    CardContent,
    CardMedia,
    Typography,
    FormControl,
    Select,
    MenuItem, AppBar, Toolbar } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import CardActionArea from '@material-ui/core/CardActionArea';
import { api } from "../../configs/configs";

const useStyles = makeStyles((theme) => ({
    root: {
        maxWidth: 345,
    },
    formControl: {
        margin: theme.spacing(1),
        minWidth: 120,
    },
    selectEmpty: {
        marginTop: theme.spacing(1),
    },
    title: {
        flexGrow: 1,
        color: "#000"
    },
}));

const Product = (prop) => {
    const classes = useStyles();
    const [products, setProducts] = useState([]);
    const [location, setLocation] = React.useState('');

    const handleChange = (event) => {
        setLocation(event.target.value)
    };

    const url = `api/product/?location=${location}`;
    useEffect(() => {
        (async () => {
            await api.get(url).then((res) => {
                if (res.status === 200) {
                    setProducts(res.data);
                }
            });
        })();
    }, [location]);

    return (
        <div>
            <AppBar position="static" style={{marginBottom: "15px"}}>
                <Toolbar style={{backgroundColor: "#cdd2ea"}}>
                    <Typography variant="h6" className={classes.title}>
                        Product List
                    </Typography>
                    <FormControl className={classes.formControl}>
                        <Select
                            value={location}
                            onChange={handleChange}
                            name = "location"
                            displayEmpty
                            className={classes.selectEmpty}
                        >
                            <MenuItem value="">
                                <em>Choose Location</em>
                            </MenuItem>
                            <MenuItem value="dhaka">Dhaka</MenuItem>
                            <MenuItem value="rajshahi">Rajshahi</MenuItem>
                            <MenuItem value="sylhet">Sylhet</MenuItem>
                            <MenuItem value="chattogram">Chattogram</MenuItem>
                        </Select>
                    </FormControl>
                </Toolbar>
            </AppBar>
            <Container maxWidth="lg">
                <div style={{display: "flex", flexDirection: "row"}}>
                    {products.map((product) => (
                        <Card className={classes.root} style={{margin: "5px"}}>
                            <CardActionArea>
                                <CardMedia
                                    component="img"
                                    alt="Contemplative Reptile"
                                    height="140"
                                    image={product.product_image[0].image}
                                    title="Contemplative Reptile"
                                />
                                <CardContent>
                                    <Typography gutterBottom variant="h5" component="h2">
                                        {product.title}
                                    </Typography>
                                    <Typography variant="body2" color="textSecondary" component="p">
                                        Price: {product.vendor_product[0].price}
                                    </Typography>
                                    <Typography variant="body2" color="textSecondary" component="p">
                                        Vendor: {product.vendor_product[0].vendor}
                                    </Typography>
                                    <Typography variant="body2" color="textSecondary" component="p">
                                        Location: {product.vendor_product[0].location}
                                    </Typography>
                                </CardContent>
                            </CardActionArea>
                        </Card>
                    ))}
                </div>
            </Container>
        </div>
    );
};

export default Product;
