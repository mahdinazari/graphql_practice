# GraphQl_practice

A `flask` project for `GraphQl` practice.

### Info
- Postgres (SqlALchemy)
- Python (Flask)

### Setup

### Models
- User
- Post


### Queries
Open `127.0.0.1:5000/api/v1/graphql-query` on browser then run below queries. 

- list all posts
```
{
  allPosts{
    edges{
      node{
        title
        body
        user{
          email
          name
        }
      }
    }
  }
}
```

