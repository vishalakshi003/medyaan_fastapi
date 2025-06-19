@strawberry.mutation
async def Createuser(self,info:Info,data:Create_user)->ResponseMessage:

        try:
            #inject dependenceny for db
            db: AsyncSession = info.context["db"]
            #validate fields with pydantic schemas
            validated = CreateUser(**data.__dict__)
            async with db.begin():
                if validated.password != validated.password1:
                    raise GraphQLError('enter correct password',extensions={"status_code":400})
                hash_password=password_context.hash(validated.password)
                emails_exists_res=await db.execute(select(CustomUser).where(CustomUser.email==validated.email))
                email_exists=emails_exists_res.scalar_one_or_none()
                if email_exists:
                    raise GraphQLError('email already exists',extensions={"status_code":400})
                
                users=CustomUser(email=validated.email,mobile_number=validated.mobile_number,password=hash_password)
                db.add(users)
                await db.commit()
                await db.refresh(users)
                await db.refresh(profile)
                return ResponseMessage(status='success',message='user created successfully')     
        except GraphQLError as gql_error:
            #  Preserve the actual GraphQL error
            raise gql_error  
        except Exception as e:
            await db.rollback()
            raise GraphQLError(f"Something went wrong :{str(e)}")
