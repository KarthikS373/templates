import mongoose, { Document, Model } from 'mongoose';

export interface IUser extends Document {
  name: string;
}

type IUserModel = Model<IUser>;

const userSchema = new mongoose.Schema<IUser>({
  name: {
    type: String,
    required: true,
    trim: true,
  },  
});

const User: Model<IUser> = mongoose.model<IUser, IUserModel>('User', userSchema);

export default User;
